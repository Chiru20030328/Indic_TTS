# TTS_7CSE4 
this is an final year project by student of presidency university of batch 2024.

We train and evaluate TTS models for 13 languages and find our models to significantly improve upon existing models in all languages as measured by mean opinion scores.

Steps:
# 1. Create environment
sudo apt-get install libsndfile1-dev ffmpeg enchant
conda create -n tts-env
conda activate tts-env

# 2. Setup PyTorch
pip3 install -U torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113

# 3. Setup Trainer
git clone https://github.com/gokulkarthik/Trainer 
cd Trainer
pip3 install -e .[all]
cd ..
[or]
cp Trainer/trainer/logging/wandb_logger.py to the local Trainer installation # fixed wandb logger
cp Trainer/trainer/trainer.py to the local Trainer installation # fixed model.module.test_log and added code to log epoch 
add `gpus = [str(gpu) for gpu in gpus]` in line 53 of trainer/distribute.py

# 4. Setup TTS
git clone https://github.com/gokulkarthik/TTS 

cd TTS
pip3 install -e .[all]
cd ..
[or]
cp TTS/TTS/bin/synthesize.py to the local TTS installation # added multiple output support for TTS.bin.synthesis

# 5. Install other requirements
pip3 install -r requirements.txt

TRAINIG STEPS:
1. Train and test by executing sh run.sh

Inference:
Trained model weight and config files can be downloaded at [this link](https://github.com/AI4Bharat/Indic-TTS/releases/tag/v1-checkpoints-release).

