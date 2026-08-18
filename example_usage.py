from client import SyntheticInstructionDatasetGeneratorClient

def main():
    client = SyntheticInstructionDatasetGeneratorClient()
    res = client.generate_dataset("Agentic Workflow Testing", 2)
    print(f"Format: {res['export_format']}")
    print(f"Diversity: {res['diversity_score_pct']}%")
    print("Samples Generated:", len(res["dataset_samples"]))
    print("Sample 1:", res["dataset_samples"][0])

if __name__ == "__main__":
    main()
