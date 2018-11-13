import os
import json
import glob
import scipy.io.wavfile
import torch.utils.data as data


class NSynth(data.Dataset):

    """Pytorch dataset for NSynth dataset
    args:
        root: root dir containing examples.json and audio directory with
            wav files.
        transform (callable, optional): A function/transform that takes in
                a sample and returns a transformed version.
        target_transform (callable, optional): A function/transform that takes
            in the target and transforms it.
    """

    def __init__(self, root, transform=None, target_transform=None):
        """Constructor"""
        self.root = root
        self.filenames = glob.glob(os.path.join(root, "audio/*.wav"))
        with open(os.path.join(root, "examples.json"), "r") as f:
            self.json_data = json.load(f)
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, index):
        """
        Args:
            index (int): Index
        Returns:
            tuple: (wav_data, json_data)
        """
        name = self.filenames[index]
        _, wav_data = scipy.io.wavfile.read(name)
        json_data = self.json_data[os.path.splitext(os.path.basename(name))[0]]
        return wav_data, json_data


if __name__ == "__main__":
    dataset = NSynth("data/nsynth-test")
    print(dataset[0])