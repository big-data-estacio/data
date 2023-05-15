mkdir -p ~/.streamlit/

echo "\
[server]\n\
handline = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml