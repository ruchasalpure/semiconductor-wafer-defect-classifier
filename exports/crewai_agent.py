from crewai import Agent

semiconductor_wafer_defect_classifier = Agent(
    role="Semiconductor Wafer Defect Classifier",
    goal="Deliver high-precision autonomous Semiconductor Wafer Defect Classifier operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
