###
 # @Author: Fantasy
 # @Date: 2020-10-31 19:21:52
 # @LastEditors: Fantasy
 # @LastEditTime: 2020-11-03 20:51:00
 # @Descripttion:
 # @Email: 776474961@qq.com
###
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/usr/local/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
        \eval "$__conda_setup"
else
        if [ -f "/usr/local/anaconda3/etc/profile.d/conda.sh" ]; then
                . "/usr/local/anaconda3/etc/profile.d/conda.sh"
                CONDA_CHANGEPS1=false conda activate base
        else
                \export PATH="/usr/local/anaconda3/bin:$PATH"
        fi
fi
unset __conda_setup
# <<< conda init <<<
. /usr/local/anaconda3/etc/profile.d/conda.sh
conda activate py3
base_dir="/home/fantasy/automatic_check_in"
cd "${base_dir}"
echo "开始上报>>>>>>>>>>>>>>>>>>>>>" >> "${base_dir}/log.log"
date >> "${base_dir}/log.log"
python main.py >> "${base_dir}/log.log"
echo "\n\n" >> "${base_dir}/log.log"
conda deactivate
conda deactivate