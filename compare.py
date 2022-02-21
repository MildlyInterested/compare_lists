import streamlit as st

st.title('Mod Whitelisting Utility')
info_text_1 = st.write('1. execute "copyToClipboard str ("true" configClasses (configFile >> "CfgPatches") apply {configName _x});" locally in the editor')
info_text_2 = st.write('2. CTRL+V in the following boxes (may freeze for a second)')
input_str_1 = st.text_input("Loaded Addons no 1")
input_str_2 = st.text_input("Loaded Addons no 2")

# compare difference between two lists and output the diff
def get_diff():
    list_1 = str(input_str_1).replace(' ','').split(',') #remove leading space from text input and make list
    list_2 = str(input_str_2).replace(' ','').split(',')
    diff = set(list_1) ^ set(list_2) #compare sets of each list and find differences
    diff_no_empty = list(filter(None, diff)) #remove empty entries and make sure it stays as list
    if len(diff_no_empty)==0:
        diff_str = 'No differences found!'
    else:
        diff_str= str(diff_no_empty).strip('{}').replace(' ','').replace('"','')
    return diff_str

diff_str = get_diff()

output_str = st.code(diff_str)

footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>Made by<a style='display: block; text-align: center;' href="https://github.com/MildlyInterested" target="_blank">Mildly Interested</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
