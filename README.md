# Task-1

## What did I do?

1. LoRA-FineTuning `T5-Large` model on a subset of amazonQA ([`#qa_Tools_and_Home_Improvement`](https://cseweb.ucsd.edu/~jmcauley/datasets/amazon/qa/)).
2. LoRA-FineTuning `Llama3-12B` model on a subset of conversation Set (`#CMU_DoG`).

## Some `Glitches` put ahead!
1. For `Conversation`, to download the `Reddit` from the [PolyAI](https://github.com/PolyAI-LDN/conversational-datasets) appears to have an error in their code, and I can't fix it, which is why I use the `#CMU_DoG`, a quite smaller Conversation-Dataset.

2. For `Conversation`, my `Llama-finetuning` always generates responses with a URL mixed in, and its responses sometimes have nothing to do with the user. (I guess it's related to the training process because I didn't train all the Training-Set, and the _'learning-rate'_ seems a little high.)
 
3*. For `metrics`, I wanted to calculate the `1-of-100 accuracy`, which is always used in LLM papers. However, after my search and study, I understand the principle but do not know how to implement it exactly like everyone does.

---

### For `QA`: `T5-Large` LoRA-Finetuning seen _`FineTuning_LoRA.ipynb`_

`T5-Large` belongs to the `Seq2SeqLM`.

#### `Configs`(train_1) of LoRA training (screenshot from Wandb)

![config1](https://github.com/Zuo-Lihan/Task-1/assets/87290137/6fac82ab-3502-45b4-b68d-c60479fdd768 "config1: train_1 (QA)")

![config2](https://github.com/Zuo-Lihan/Task-1/assets/87290137/1cdcbc66-b53a-412c-b39e-14c35d4bb161 "config2: train_1 (QA)")

![basic](https://github.com/Zuo-Lihan/Task-1/assets/87290137/6dfa1ec5-868d-4117-932d-0455b20f8e69 "basic w results: train_1 (QA)")

#### `Training Loss`

![train loss](https://github.com/Zuo-Lihan/Task-1/assets/87290137/e3ad836e-9da6-4c80-9b3d-648728f92662 "Train Loss (QA)")

#### `Results`

![Results](https://github.com/Zuo-Lihan/Task-1/assets/87290137/de33c5c3-99ff-49d2-93ee-c96e140c008b "Results: train_1 (QA)")

---

### For `Conversation`: `Llama3-12B` LoRA-Finetuning seen in _`/communication_G/LlaMA3 Communication_LoRA_G (right).ipynb`_

`Llama3` belongs to the `CausalLM`.

#### `Configs` (Llama3-train) of LoRA training (screenshot from wandb)

![config1](https://github.com/Zuo-Lihan/Task-1/assets/87290137/8bf65828-26ef-4b77-a235-2e02930cd53a "config1: Llama3-train (Conversation)")

![config2](https://github.com/Zuo-Lihan/Task-1/assets/87290137/2434cff5-f134-4987-9dba-c739e1af06e7 "config2: Llama3-train (Conversation)")

![basic](https://github.com/Zuo-Lihan/Task-1/assets/87290137/5e954720-1363-42f2-887b-08eeb669f76b "basic w/o result: Llama3-train (Conversation)")

#### `Train Loss`

![train loss](https://github.com/Zuo-Lihan/Task-1/assets/87290137/f5c774d6-dcc6-4011-a830-47f5d1562a1c "train_loss (Conversation)")

#### `Results`

![response](https://github.com/Zuo-Lihan/Task-1/assets/87290137/bc6069bb-60da-459d-9532-01e24f617e59 "response example (Conversation)")


I didn't run the `metrics` for **Conversation-Dataset Finetuning**.








