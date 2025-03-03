from typing import List, Dict, Any
import yaml
import os

class AgentDesigner:
    def __init__(self):
        self.templates = {
            "basic": {
                "name": "Basic Agent",
                "description": "Simple agent with basic capabilities",
                "requirements": {
                    "memory": "2GB",
                    "cpu_cores": 2,
                    "python_packages": ["requests", "python-dotenv"]
                },
                "features": [
                    "HTTP requests",
                    "Environment variable management",
                    "Basic error handling"
                ]
            },
            "advanced": {
                "name": "Advanced Agent",
                "description": "Advanced agent with ML capabilities",
                "requirements": {
                    "memory": "8GB",
                    "cpu_cores": 4,
                    "python_packages": [
                        "torch",
                        "transformers",
                        "numpy",
                        "pandas"
                    ]
                },
                "features": [
                    "Machine learning inference",
                    "Data processing",
                    "Advanced error handling",
                    "Logging and monitoring"
                ]
            }
        }

    def get_templates(self) -> Dict[str, Any]:
        """Get available agent templates"""
        return self.templates

    def create_agent_config(self, template_name: str, customizations: Dict[str, Any]) -> Dict[str, Any]:
        """Create agent configuration based on template and customizations"""
        if template_name not in self.templates:
            raise ValueError(f"Template {template_name} not found")

        base_config = self.templates[template_name].copy()
        for key, value in customizations.items():
            if key in base_config:
                if isinstance(base_config[key], dict):
                    base_config[key].update(value)
                else:
                    base_config[key] = value

        return base_config

    def generate_agent_code(self, config: Dict[str, Any]) -> str:
        """Generate Python code for the agent based on configuration"""
        code = f"""
import os
import logging
from typing import Any, Dict

class {config['name'].replace(' ', '')}:
    def __init__(self):
        self.name = "{config['name']}"
        self.logger = self._setup_logging()
        
    def _setup_logging(self) -> logging.Logger:
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info(f"Processing input: {{input_data}}")
        try:
            # Add custom processing logic here
            result = {{"status": "success", "data": input_data}}
            return result
        except Exception as e:
            self.logger.error(f"Error processing input: {{str(e)}}")
            return {{"status": "error", "message": str(e)}}

if __name__ == "__main__":
    agent = {config['name'].replace(' ', '')}()
    result = agent.run({{"test": "data"}})
    print(result)
"""
        return code

    def save_agent(self, name: str, config: Dict[str, Any], output_dir: str) -> str:
        """Save agent configuration and code to files"""
        os.makedirs(output_dir, exist_ok=True)
        
        # Save configuration
        config_path = os.path.join(output_dir, f"{name}_config.yaml")
        with open(config_path, 'w') as f:
            yaml.dump(config, f)
        
        # Save agent code
        code = self.generate_agent_code(config)
        code_path = os.path.join(output_dir, f"{name}.py")
        with open(code_path, 'w') as f:
            f.write(code)
            
        return code_path

    def get_deployment_checklist(self, config: Dict[str, Any]) -> List[str]:
        """Generate deployment checklist based on agent configuration"""
        checklist = [
            "Verify system meets minimum requirements:",
            f"- RAM: {config['requirements']['memory']}",
            f"- CPU Cores: {config['requirements']['cpu_cores']}"
        ]
        
        if 'python_packages' in config['requirements']:
            checklist.append("\nInstall required packages:")
            for package in config['requirements']['python_packages']:
                checklist.append(f"- pip install {package}")
        
        checklist.extend([
            "\nDeployment steps:",
            "1. Create virtual environment",
            "2. Install dependencies",
            "3. Configure environment variables",
            "4. Test agent functionality",
            "5. Setup monitoring (if applicable)",
            "6. Configure error reporting"
        ])
        
        return checklist

    def validate_system_compatibility(self, config: Dict[str, Any], system_info: Dict[str, Any]) -> List[str]:
        """Validate if the system meets agent requirements"""
        issues = []
        
        # Check memory
        required_memory = float(config['requirements']['memory'].replace('GB', ''))
        system_memory = system_info['hardware_info']['total_memory'] / (1024 ** 3)
        if system_memory < required_memory:
            issues.append(f"Insufficient memory: {system_memory:.1f}GB available, {required_memory}GB required")

        # Check CPU cores
        required_cores = config['requirements']['cpu_cores']
        system_cores = system_info['hardware_info']['cpu_cores']
        if system_cores < required_cores:
            issues.append(f"Insufficient CPU cores: {system_cores} available, {required_cores} required")

        return issues
