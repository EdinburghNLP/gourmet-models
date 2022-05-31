## Model list

| Language pair | Version | Link |
| --------------- | --------------- | --------------- |
| Bulgarian to English | 0.1 | http://data.statmt.org/gourmet/models/docker/bg-en.20190801.tgz |
| English to Bulgarian  | 0.2 | http://data.statmt.org/gourmet/models/docker/en-bg.v0.2.tgz |
| Gujarati to English | 0.1 | http://data.statmt.org/gourmet/models/docker/gu-en.20190628.tgz |
| English to Gujarati | 0.2 | http://data.statmt.org/gourmet/models/docker/en-gu.v0.2.tgz  |
| Swahili to English | 0.5 | https://data.statmt.org/gourmet/models/docker/translation-sw-en-0-5-0.docker.gz |
| English to Swahili | 0.5 | https://data.statmt.org/gourmet/models/docker/translation-en-sw-0-5-0.docker.gz |
| Tamil to English | 0.1  | http://data.statmt.org/gourmet/models/docker/mt-engine-ta-en.tar.gz |
| English to Tamil | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-ta.tar.gz |
| Serbian to English | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-sr-en.tar.gz |
| English to Serbian (Cyrilic) | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-sr.cyr.tar.gz  |
| English to Serbian (Latin) | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-sr.lat.tar.gz |
| Hausa to English | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-ha-en.v0.2.tar.gz  |
| English to Hausa | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-ha.v0.2.tar.gz |
| Igbo to English | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-ig-en.v0.2.tar.gz |
|  English to Igbo | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-ig.v0.2.tar.gz |
| Pashto to English | 0.4.1 | https://data.statmt.org/gourmet/models/docker/translation-ps-en-0-4-1.docker.gz |
| English to Pashto | 0.4.1 | https://data.statmt.org/gourmet/models/docker/translation-en-ps-0-4-1.docker.gz |
| Turkish to English | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-tr-en.tgz |
| English to Turkis | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-tr.tgz|
| Turkish to English | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-v2-tr-en.tgz|
| English to Turkish | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-v2-en-tr.tgz |
| Amharic to English | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-am-en.tgz|
| English to Amharic | 0.1 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-am.tgz|
| Kyrgyz to English | 0.1.1 | https://data.statmt.org/gourmet/models/docker/translation-ky-en-0-1-1.docker.gz |
| English to Kyrgyz | 0.1.1 | https://data.statmt.org/gourmet/models/docker/translation-en-ky-0-1-1.docker.gz |
| Macedonian to English | 0.1.1 | https://data.statmt.org/gourmet/models/docker/translation-mk-en-0-1-1.docker.gz |
| English to Macedonian | 0.1.2 | https://data.statmt.org/gourmet/models/docker/translation-en-mk-0-1-2.docker.gz |
| Urdu to English | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-ur-en.v0.2.tar.gz|
| English to Urdu | 0.2 | http://data.statmt.org/gourmet/models/docker/mt-engine-en-ur.v0.2.tar.gz|
| Myanmar to English | 0.1 Slower  | http://data.statmt.org/gourmet/models/docker/translation-my-en-slower-0-1-0.docker.gz |
| English to Myanmar | 0.1 Slower | http://data.statmt.org/gourmet/models/docker/translation-en-my-slower-0-1-0.docker.gz |
| Myanmar to English | 0.1 Faster  | http://data.statmt.org/gourmet/models/docker/translation-my-en-faster-0-1-0.docker.gz |
| English to Myanmar | 0.2.3 Faster  | https://data.statmt.org/gourmet/models/docker/translation-en-my-faster-0-2-3.docker.gz |
| Yoruba to English | 0.1 | https://data.statmt.org/gourmet/models/docker/mt-engine-yo-en.tgz |
| English to Yoruba | 0.1 | https://data.statmt.org/gourmet/models/docker/mt-engine-en-yo.tgz |


## Additional Arguments

The following are supported by en>bg, en>gu, en<>ig, en<>ha , using the `-e` argument to docker 

`DEBUG` - Set this to anything to get more verbosity

`MARIAN_THREADS` - defaults to 1, but increase this to get the translator to use more threads. This will only be useful if your translation job contains several sentences.

`MARIAN_BATCH` - defaults to 1, but increase this for larger translation jobs


