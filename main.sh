###
 # @Author: Fantasy
 # @Date: 2020-10-31 19:21:52
 # @LastEditors  : Please set LastEditors
 # @LastEditTime : 2022-04-10 21:16:01
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
conda activate safety_report
base_dir="/home/fantasy/safety_report"
cd "${base_dir}"
echo "开始上报>>>>>>>>>>>>>>>>>>>>>"
date
python main.py
echo "上报结束====================="
conda deactivate
conda deactivate