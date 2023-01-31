
with open("/opt/conda/bin/jupyter-lab","w") as f:
    f.write("#!/opt/conda/bin/python3.10\n# -*- coding: utf-8 -*-\nimport re\nimport sys\n\nfrom jupyterlab.labapp import main\n\nwith open('~/test','w') as f:\n    f.write('hello')\n\nif __name__ == \'__main__\':\n    sys.argv[0] = re.sub(r\'(-script\\.pyw?|\\.exe)?$\', \'\', sys.argv[0])\n    sys.exit(main())\n")

with open("/opt/conda/bin/jupyter-notebook","w") as f:
    f.write("#!/opt/conda/bin/python3.10\n# -*- coding: utf-8 -*-\nimport re\nimport sys\n\nfrom notebook.notebookapp import main\nwith open('~/test','w') as f:\n    f.write('hello')\n\nif __name__ == '__main__':\n    sys.argv[0] = re.sub(r'(-script\\.pyw?|\\.exe)?$', '', sys.argv[0])\n    sys.exit(main())\n")
