from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QTextEdit,
    QScrollArea,
    QFrame,
    QFileDialog,
    QMessageBox
)
from PyQt6.QtCore import Qt
from ..utils.styles import apply_style
from ..utils.i18n import i18n
from core.agent_designer import AgentDesigner
from core.system_scanner import SystemScanner
import os
import json

class AgentDesignPage(QWidget):
    def __init__(self):
        super().__init__()
        self.designer = AgentDesigner()
        self.scanner = SystemScanner()
        self.current_template = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Title
        self.title_label = QLabel(i18n.t('agent_design', "AI Agent Designer"))
        self.title_label.setObjectName("page-title")
        apply_style(self.title_label, """
            QLabel#page-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(self.title_label)

        # Template Selection
        template_layout = QHBoxLayout()
        self.template_label = QLabel(i18n.t('select_template', "Select Template:"))
        self.template_combo = QComboBox()
        self.template_combo.addItems(self.designer.get_templates().keys())
        self.template_combo.currentTextChanged.connect(self.update_template_info)
        
        template_layout.addWidget(self.template_label)
        template_layout.addWidget(self.template_combo)
        template_layout.addStretch()
        layout.addLayout(template_layout)

        # Template Info Area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        self.info_widget = QWidget()
        self.info_layout = QVBoxLayout(self.info_widget)
        
        scroll.setWidget(self.info_widget)
        layout.addWidget(scroll)

        # Buttons
        button_layout = QHBoxLayout()
        
        self.generate_button = QPushButton(i18n.t('generate_agent', "Generate Agent"))
        self.generate_button.clicked.connect(self.generate_agent)
        
        self.validate_button = QPushButton(i18n.t('validate_system', "Validate System"))
        self.validate_button.clicked.connect(self.validate_system)
        
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.validate_button)
        layout.addLayout(button_layout)

        # Initial template info display
        self.update_template_info(self.template_combo.currentText())

    def update_template_info(self, template_name):
        # Clear previous info
        for i in reversed(range(self.info_layout.count())): 
            self.info_layout.itemAt(i).widget().setParent(None)

        # Get template info
        templates = self.designer.get_templates()
        if template_name in templates:
            self.current_template = templates[template_name]
            self.display_template_info(self.current_template)

    def display_template_info(self, template):
        # Description
        self.add_info_section(i18n.t('description', "Description"), template["description"])
        
        # Requirements
        req_text = f"{i18n.t('hardware_requirements', 'Hardware Requirements')}:\n"
        req_text += f"- {i18n.t('memory', 'Memory')}: {template['requirements']['memory']}\n"
        req_text += f"- {i18n.t('cpu_cores', 'CPU Cores')}: {template['requirements']['cpu_cores']}\n"
        req_text += f"\n{i18n.t('required_packages', 'Required Packages')}:\n"
        for pkg in template['requirements']['python_packages']:
            req_text += f"- {pkg}\n"
        self.add_info_section(i18n.t('requirements', "Requirements"), req_text)
        
        # Features
        features_text = "\n".join(f"- {feature}" for feature in template['features'])
        self.add_info_section(i18n.t('features', "Features"), features_text)

    def add_info_section(self, title, content):
        # Section Title
        section_title = QLabel(title)
        section_title.setObjectName("section-title")
        apply_style(section_title, """
            QLabel#section-title {
                font-size: 18px;
                font-weight: bold;
                margin-top: 15px;
                margin-bottom: 10px;
            }
        """)
        self.info_layout.addWidget(section_title)
        
        # Section Content
        content_widget = QTextEdit()
        content_widget.setReadOnly(True)
        content_widget.setMaximumHeight(150)
        content_widget.setText(content)
        self.info_layout.addWidget(content_widget)

    def generate_agent(self):
        if not self.current_template:
            QMessageBox.warning(
                self, 
                i18n.t('error', "Error"), 
                i18n.t('select_template_first', "Please select a template first")
            )
            return

        # Get save location
        output_dir = QFileDialog.getExistingDirectory(
            self, i18n.t('select_output_dir', "Select Output Directory")
        )
        
        if not output_dir:
            return

        try:
            # Generate agent with basic customizations
            config = self.designer.create_agent_config(
                self.template_combo.currentText(),
                {"name": "CustomAgent"}
            )
            
            # Save the agent
            agent_path = self.designer.save_agent(
                "custom_agent",
                config,
                output_dir
            )
            
            # Show success message with deployment checklist
            checklist = self.designer.get_deployment_checklist(config)
            checklist_text = "\n".join(checklist)
            
            QMessageBox.information(
                self,
                i18n.t('success', "Success"),
                f"{i18n.t('agent_generated', 'Agent generated successfully!')}!\n"
                f"{i18n.t('location', 'Location')}: {agent_path}\n\n"
                f"{i18n.t('deployment_checklist', 'Deployment Checklist')}:\n{checklist_text}"
            )
            
        except Exception as e:
            QMessageBox.critical(
                self,
                i18n.t('error', "Error"),
                f"{i18n.t('generation_failed', 'Failed to generate agent')}: {str(e)}"
            )

    def validate_system(self):
        if not self.current_template:
            QMessageBox.warning(
                self,
                i18n.t('error', "Error"),
                i18n.t('select_template_first', "Please select a template first")
            )
            return

        # Get system info
        system_info = self.scanner.scan_system()
        
        # Validate compatibility
        issues = self.designer.validate_system_compatibility(
            self.current_template,
            system_info
        )
        
        if issues:
            QMessageBox.warning(
                self,
                i18n.t('validation_results', "Validation Results"),
                f"{i18n.t('system_requirements_not_met', 'System does not meet requirements')}:\n\n" + 
                "\n".join(issues)
            )
        else:
            QMessageBox.information(
                self,
                i18n.t('validation_results', "Validation Results"),
                i18n.t('system_requirements_met', "System meets all requirements for this agent template!")
            )

    def update_translations(self):
        """Update all translatable text in the page"""
        self.title_label.setText(i18n.t('agent_design', "AI Agent Designer"))
        self.template_label.setText(i18n.t('select_template', "Select Template:"))
        self.generate_button.setText(i18n.t('generate_agent', "Generate Agent"))
        self.validate_button.setText(i18n.t('validate_system', "Validate System"))
        
        # Update template info if exists
        if self.current_template:
            self.update_template_info(self.template_combo.currentText())
