import os
import sys

temp_file_name = sys.argv[1]

os.system(f'cd ../ && flutter create {temp_file_name} && cd ./{temp_file_name}/lib && mkdir domain infrastructure presentation config core && cd domain && mkdir entities repositories datasources && cd ../infrastructure/ &&  mkdir datasources repositories models mappers && cd ../presentation/ && mkdir providers screens views widgets && cd ../config/ && mkdir constants router theme && touch config.dart && cd ./constants/ && touch environment.dart')