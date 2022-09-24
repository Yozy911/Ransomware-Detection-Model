# Ransomware-Detection-Model
Machine learning based detection framework to detect ransomware on windows OS. This repository does not
include the cuckoo sandbox API that is purposed for submitting a sample to cuckoo sandbox for dynamic 
analysis and retreiving a json report. Rather, the samples tested were manually submitted to cuckoo 
and the json reports were retrieved which are the seed that the framework works with. The user interface
is implemented using streamlit (refer to 'https://docs.streamlit.io/library/get-started/installation' to 
ensure all dependancies are up-to-date).


Please cite my work when using either a component or all:
Mkandawire, Y. (2022). Host-Based ransomware detection framework with machine learnign [Unpublished manuscript]. Mulungushi University


NOTE!!
This projects uses the dataset generated from the works of Daniele Sgandurra, 
Luis Muñoz-González, Rabih Mohsen, Emil C. Lupu. Please, reference their work when using this dataset:

Daniele Sgandurra, Luis Muñoz-González, Rabih Mohsen, Emil C. Lupu. 
"Automated Dynamic Analysis of Ransomware: Benefits, Limitations and use for Detection." 
arXiv preprint arXiv:1609.03020, 2016.

For BIBTEX you can use this:

@article{sgandurra2016,
  title={{Automated Dynamic Analysis of Ransomware: Benefits, Limitations and use for Detection}},
  author={Sgandurra, Daniele and Mu{\~n}oz-Gonz{\'a}lez, Luis and Mohsen, Rabih and Lupu, Emil C},
  journal={arXiv preprint arXiv:1609.03020},
  year={2016}
}
