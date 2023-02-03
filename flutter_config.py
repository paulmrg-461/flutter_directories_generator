import os
import sys

temp_file_name = sys.argv[1]

os.system(f'flutter create {temp_file_name} && cd ./{temp_file_name}/lib && mkdir domain data ui device && cd domain && mkdir entities bloc repositories services && cd ../data/ &&  mkdir repositories services && cd ../ui/ && mkdir screens shared themes routes')