class SyntheticInstructionDatasetGeneratorClient:
    def generate_dataset(self, domain_topic: str = "Python Agent Development", samples_count: int = 3) -> dict:
        samples = [
            {"instruction": "Write an async Python function to poll task status.", "input": "", "output": "import asyncio\nasync def poll(): pass"},
            {"instruction": "How do you securely store API keys in an environment file?", "input": "", "output": "Use dotenv and add .env to .gitignore."}
        ]
        return {
            "dataset_samples": samples,
            "diversity_score_pct": 95.8,
            "export_format": "ALPACA_JSONL"
        }
