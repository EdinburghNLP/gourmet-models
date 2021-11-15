# Gourmet Models

## Overview
The [Gourmet](https://gourmet-project.eu) has released several machine translation models to translate low-resource languages. This repository
contains information about the models, as well as sample code showing how the models can be used. The models themselves are available as dockers, and
can be downloaded from a separate site (see below).


## Using the Models

The model download links are [here](https://github.com/EdinburghNLP/gourmet-models/blob/main/models.md). Once downloaded, the model
can be loaded using:
```
docker load < <MODEL_FILE>
```
to launch the translation server, use:

```
docker run -p 4000:4000 -i --rm <MODEL_NAME>
```
This exposes the model on port 4000. Change the second number above if you want to use a different port.
