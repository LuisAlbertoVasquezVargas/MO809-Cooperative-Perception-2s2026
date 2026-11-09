# Appendix Source Coverage

Presentation date: **November 5, 2026**. The original 29 talk pages precede the appendix.

Include all weekly technical slides and every experiments-report page. Weekly task, progress, and planning pages are excluded at the user's request, along with weekly navigation, duplicate covers, and closing; full-detail variants of technical material summarized in the main talk are retained.

Embed original PDF pages without rasterization or redrawing. Replace weekly counters with appendix counters; replace report footer pagination with a source-page label. No new inference, training, or measurement.

| Appendix Pages | PDF Pages | Section | Source Pages |
| --- | --- | --- | --- |
| A3–A26 | 32–55 | A. Architecture and Implementation | weekly: 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33 |
| A27–A37 | 56–66 | B. Evaluation and Reproduction | weekly: 35, 36, 37, 38, 39, 40, 41, 42, 43, 44 |
| A38–A58 | 67–87 | C. Conv2D and Conv3D | weekly: 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 |
| A59–A79 | 88–108 | D. Complete Experiment Record | experiments: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 |
| A80–A83 | 109–112 | E. Image Generation Example | Native LaTeX: Simple Workflow, Prompt: Generate the Image, Generated Result |

Total: **83 appendix pages**, **112 PDF pages**.

## Page-by-Page Mapping

| Appendix Page | PDF Page | Source Page | Original Title |
| --- | --- | --- | --- |
| A4 | 33 | weekly 7 | LiDAR Preprocessing |
| A5 | 34 | weekly 8 | Voxelization |
| A6 | 35 | weekly 10 | Normalization and Activation |
| A7 | 36 | weekly 11 | 2D Unit |
| A8 | 37 | weekly 12 | 2D Unit: Variants |
| A9 | 38 | weekly 13 | 2D Pointwise Unit |
| A10 | 39 | weekly 14 | Decoder Block |
| A11 | 40 | weekly 15 | 3D Convolution |
| A12 | 41 | weekly 16 | Encoder Stage |
| A13 | 42 | weekly 17 | Upsample and Concat |
| A14 | 43 | weekly 18 | Decoder Stage |
| A15 | 44 | weekly 20 | Encoder Pipeline |
| A16 | 45 | weekly 21 | Encoder Code |
| A17 | 46 | weekly 23 | DiscoGraph |
| A18 | 47 | weekly 24 | DiscoGraph: Feature Alignment |
| A19 | 48 | weekly 25 | DiscoGraph: Rotate and Translate |
| A20 | 49 | weekly 26 | DiscoGraph: Alignment in PyTorch |
| A21 | 50 | weekly 27 | DiscoGraph: Pair the Features |
| A22 | 51 | weekly 28 | DiscoGraph: Edge Scores |
| A23 | 52 | weekly 29 | DiscoGraph: Spatial Weights |
| A24 | 53 | weekly 30 | DiscoGraph: Weighted Features |
| A25 | 54 | weekly 31 | DiscoGraph: Fused Features |
| A26 | 55 | weekly 33 | Decoder Pipeline |
| A28 | 57 | weekly 35 | Intersection over Union (IoU) |
| A29 | 58 | weekly 36 | IoU: Matching Thresholds |
| A30 | 59 | weekly 37 | DiscoNet Confidence Scores |
| A31 | 60 | weekly 38 | Precision, Recall, and AP |
| A32 | 61 | weekly 39 | V2X-Sim 2.0: Dataset Analysis |
| A33 | 62 | weekly 40 | V2X-Sim 2.0: Car Detections |
| A34 | 63 | weekly 41 | V2X-Sim 2.0: Camera Views |
| A35 | 64 | weekly 42 | Experiment Setup |
| A36 | 65 | weekly 43 | V2X-Sim 2.0: Reproduced Results |
| A37 | 66 | weekly 44 | V2X-Sim 2.0: Runtime Scaling |
| A39 | 68 | weekly 50 | Initial Tensor |
| A40 | 69 | weekly 51 | Kernels |
| A41 | 70 | weekly 52 | Conv2D: Sliding Window |
| A42 | 71 | weekly 53 | Conv2D: Sliding Window |
| A43 | 72 | weekly 54 | Conv2D: Sliding Window |
| A44 | 73 | weekly 55 | Conv2D: Sliding Window |
| A45 | 74 | weekly 56 | Conv2D: Sliding Window |
| A46 | 75 | weekly 57 | Conv2D: Sliding Window |
| A47 | 76 | weekly 58 | Conv3D: Sliding Window |
| A48 | 77 | weekly 59 | Conv3D: Sliding Window |
| A49 | 78 | weekly 60 | Conv3D: Sliding Window |
| A50 | 79 | weekly 61 | Conv3D: Sliding Window |
| A51 | 80 | weekly 62 | Conv3D: Sliding Window |
| A52 | 81 | weekly 63 | Conv3D: Sliding Window |
| A53 | 82 | weekly 64 | Conv3D: Sliding Window |
| A54 | 83 | weekly 65 | Conv3D: Sliding Window |
| A55 | 84 | weekly 66 | Conv3D: Sliding Window |
| A56 | 85 | weekly 67 | Conv3D: Sliding Window |
| A57 | 86 | weekly 68 | Conv3D: Sliding Window |
| A58 | 87 | weekly 69 | Conv3D: Sliding Window |
| A60 | 89 | experiments 1 | DiscoNet: Our First Experiment |
| A61 | 90 | experiments 2 | Example 1: Reference and Predicted Car Boxes |
| A62 | 91 | experiments 3 | Example 1: Camera Views |
| A63 | 92 | experiments 4 | V2X-Sim 2.0: Dataset Overview |
| A64 | 93 | experiments 5 | Authors' Training Setup and Dataset Splits |
| A65 | 94 | experiments 6 | Dataset Statistics by Partition and Vehicle Inputs |
| A66 | 95 | experiments 7 | Experiment Setup: Hardware and Software |
| A67 | 96 | experiments 8 | Experiment Procedure, Metrics, and Running Time |
| A68 | 97 | experiments 9 | Original Test Split: Loss and Detection Accuracy |
| A69 | 98 | experiments 10 | How DiscoNet Computes Confidence Scores |
| A70 | 99 | experiments 11 | How Precision–Recall Curves and AP Are Computed |
| A71 | 100 | experiments 12 | Original Test Split: Accuracy and Loss Plots |
| A72 | 101 | experiments 13 | Custom Experiments |
| A73 | 102 | experiments 14 | Custom Experiment 1: V2X-Sim Inputs and Replay |
| A74 | 103 | experiments 15 | Custom Experiment 1: Measuring Runtime |
| A75 | 104 | experiments 16 | Custom Experiment 1: Runtime Results for n = 1–10 |
| A76 | 105 | experiments 17 | Custom Experiment 1: Runtime Results for n = 11–20 |
| A77 | 106 | experiments 18 | Custom Experiment 1: Runtime Versus Model Input Count |
| A78 | 107 | experiments 19 | Custom Experiment 2: Coarse Attention and Kruskal Fusion |
| A79 | 108 | experiments 20 | Custom Experiment 2: Runtime and Detection AP |
| A81 | 110 | Native LaTeX | Simple Workflow |
| A82 | 111 | Native LaTeX | Prompt: Generate the Image |
| A83 | 112 | Native LaTeX | Generated Result |

## Excluded Weekly Pages

| Source Page | Reason |
| --- | --- |
| 1 | Weekly cover; MO809 cover and presentation date are retained. |
| 2 | Weekly agenda; replaced by the appendix contents. |
| 3 | Current Steps section cover; its research-context content is excluded. |
| 4 | Weekly research task, progress, or planning; removed with Appendix E at the user's request. |
| 5 | Weekly research task, progress, or planning; removed with Appendix E at the user's request. |
| 6 | Preprocessing section cover; grouped under Architecture and Implementation. |
| 9 | Reusable Blocks section cover; grouped under Architecture and Implementation. |
| 19 | Encoder section cover; grouped under Architecture and Implementation. |
| 22 | DiscoGraph section cover; grouped under Architecture and Implementation. |
| 32 | Decoder section cover; grouped under Architecture and Implementation. |
| 34 | Experiments section cover; replaced by Evaluation and Reproduction. |
| 45 | Next Steps section cover; its research-planning content is excluded. |
| 46 | Weekly research task, progress, or planning; removed with Appendix E at the user's request. |
| 47 | Weekly research task, progress, or planning; removed with Appendix E at the user's request. |
| 48 | Weekly closing; the original MO809 closing is retained. |
| 49 | Convolution appendix cover; replaced by Conv2D and Conv3D. |

All 20 experiments-report pages are included, including its custom-experiments divider. Content summarized in the main talk is retained in full here so the appendix is complete.
