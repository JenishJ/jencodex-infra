# JenCodeX Enterprise Model Architecture

## Cluster Strategy
- **Node 1 (Heavy):** 8x H200 (Passthrough) -> For 70B+ Models
- **Node 2 (Retail):** 8x H200 (MIG Sliced) -> For Devs & Small Agents

## Approved Enterprise Models

| Model Name | Size | Type | Node Assignment | VRAM Needed |
| :--- | :--- | :--- | :--- | :--- |
| **Qwen-2.5-Coder-32B** | 32B | Coding Agent | Node 2 (MIG) | ~20 GB (INT4) |
| **Llama-3-70B** | 70B | General Chat | Node 1 (Full) | ~40 GB (INT4) / 140GB (FP16) |
| **DeepSeek-V3** | 671B | Reasoning | Node 1 (Full) | ~650 GB (FP8) |
| **Llama-3-405B** | 405B | Master Brain | Node 1 (Full) | ~800 GB (FP8) |

## Resource Limits (Kubernetes)
- **Small Job:** `nvidia.com/mig-1g.20gb: 1` + `memory: 8Gi`
- **Big Job:** `nvidia.com/gpu: 1` + `memory: 200Gi`