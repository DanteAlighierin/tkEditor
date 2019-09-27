try:
       import editor

except ImportError as e:
       import sys
       sys.exit("editor.py module missing.")

if __name__ == '__main__':
       edit = editor.Editor()
       edit.editor()