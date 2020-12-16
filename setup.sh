mkdir -p ~ / .streamlit /
echo “\ 
[general] \ n \ 
email = \” rociorodriguezsc@gmail.com \ ”\ n \ 
“> ~ / .streamlit / credentials.toml
echo “\ 
[servidor] \ n \ 
headless = true \ n \ 
enableCORS = false \ n \ 
port = $ PORT \ n \ 
“> ~ / .streamlit / config.toml