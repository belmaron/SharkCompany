import json,re,sys
m=json.load(open(sys.argv[1]))
src=open('src/site.html').read().replace('/*VIEWS*/{}',json.dumps({int(k):v for k,v in m.items()},ensure_ascii=False))
# open('artifact.html','w').write(src)  # versão para o artefato do Claude
title,rest=src.split('\n',1)
open('index.html','w').write('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+title+'\n'+rest.replace('<nav class','</head>\n<body>\n<nav class',1)+'\n</body>\n</html>\n')
