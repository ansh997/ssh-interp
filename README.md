# Team24-SSH: \<ssh-interp>
    Himanshu Pal 2023701003
    Snigdha Agarwal  2023701013
    Uday Bhaskar

```bash
# Create a new conda environment
conda create -n vl python=3.9
conda activate vl

# Set up LLaVA repo
mkdir src/caption/llava
cd src/caption/llava
git clone https://github.com/haotian-liu/LLaVA.git
cd LLaVA
pip3 install -e .

# cd back into repo root
cd ../../../../
pip3 install -e .

# Install some remaining packages
pip3 install lightning openai-clip transformers==4.37.2 omegaconf python-dotenv "numpy<2"
```

## Model Weights
The model weights for LlaVA are automatically downloaded from hugging face.

The configs for InstructBLIP models are under `src/caption/lavis/configs/`. In order to get InstructBLIP (7B) working, you should download the [pretrained model weights](https://storage.googleapis.com/sfr-vision-language-research/LAVIS/models/InstructBLIP/instruct_blip_vicuna7b_trimmed.pth) and [vicuna7b weights](https://huggingface.co/lmsys/vicuna-7b-v1.1) weights. In `src/caption/lavis/configs/blip2_instruct_vicuna7b.yaml`, set the pretrained location to the pretrained weight path and llm_model to the vicuna7b weight path.