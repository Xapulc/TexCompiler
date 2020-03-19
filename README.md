## Preview

This unix command-line tool can help manage TeX directories
with enumerated files.
It can 
* compile tex to pdf, delete aux files;
* edit project in your text editor;
* create new tex document from given pattern;
* open pdf result file in your viewer.

## Configuration

It is needed to create `subjects.yaml`, for example
```
add_pt:
  pdf: "lectureAddTopics"                             # name of pdf, optionally
  title: "Lecture"                                    # title with number in tex, optionally
  desc: "Additional topics of Probability Theory"     # description of subject
  path: "/home/user/study/AddTopicsProbabilityTheory" # work folder
st_proc:
  pdf: "seminarMS" 
  title: "Seminar"
  desc: "Mathematical statistics"
  path: "/home/user/study/StatisticalTheory"
```
Also you can configure `default_config.yaml`.

## Requirements

You should install `latexmk` and `python3>=3.6`.