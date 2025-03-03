from setuptools import setup, find_packages

setup(
    name="ai-agent-assistant",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.4.0",
        "psutil>=5.9.0",
        "requests>=2.28.0",
        "python-dotenv>=0.19.0",
        "SQLAlchemy>=1.4.0",
        "PyYAML>=6.0",
        "rich>=12.0.0"
    ],
    entry_points={
        "console_scripts": [
            "ai-agent-assistant=src.main:main",
        ],
    },
    author="TsungLun Ho",
    description="A tool for analyzing system usage patterns and designing AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="ai, agent, system analysis, performance monitoring",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
        "Topic :: System :: Systems Administration",
    ],
)
