from pathlib import Path
from typing import Literal

import pytest
import sources.main as fm
import os

@pytest.mark.parametrize("filename, ext",[("anmol.pdf","PDFs"),("dikshu.py","Code"),("dishu.jpg","Images"),("golu.csv","TextFiles"),("icpc.py","Code")])
def test_get_catagory(filename: Literal['anmol.pdf'] | Literal['dikshu.py'] | Literal['dishu.jpg'] | Literal['golu.csv'] | Literal['icpc.py'],ext: Literal['PDFs'] | Literal['Code'] | Literal['Images'] | Literal['TextFiles']):
    assert fm.get_category(filename) == ext

def test_create_folders(tmp_path: Path):
    folders = ["Images",
               "PDFs",
               "TextFiles"
               ,"Music",
               "Videos",
               "Documents",
               "Code",
               "Others"]
    fm.create_folders(tmp_path)
    for folder in folders:
        assert (tmp_path/folder).exists()



def test_organize_no_file(tmp_path):
    assert fm.organize(tmp_path) == None

def test_organize(tmp_path):
    (tmp_path/"anmol.jpg").touch()
    (tmp_path/"ab.png").touch()
    (tmp_path/"an.pdf").touch()
    (tmp_path/"al.csv").touch()
    (tmp_path/"ad.txt").touch()
    (tmp_path/"aa.py").touch()
    fm.create_folders(tmp_path)
    fm.organize(tmp_path)

    filename = ["anmol.jpg",
                "ab.png",
                "an.pdf",
                "al.csv",
                "ad.txt",
                "aa.py"]
    for file in filename:
        assert (tmp_path/fm.get_category(file)/file).exists()

def test_get_cat_path(tmp_path, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: tmp_path)

    assert fm.get_cat_path() == tmp_path

def test_get_cat_path_not_a_folder(tmp_path,monkeypatch):
    (tmp_path/"Dikshu.py").touch()
    path = str(tmp_path/"Dikshu.py")
    monkeypatch.setattr("builtins.input", lambda _: path)
    
    assert fm.get_cat_path() == None

def test_get_cat_path_for_invalid_path(tmp_path, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Anmol")

    assert fm.get_cat_path() == None

def test_log_mov_exist(tmp_path):
    log_path = str(tmp_path/"log.txt")
    fm.log_move("Dikshu.jpg","Images",log_path)

    assert os.path.exists(log_path)

def test_log_move_writes_correct_content(tmp_path):
    log_path = str(tmp_path/"log.txt")
    fm.log_move("Dikshu.png","Images",log_path)
    with open(log_path, "r",encoding="utf-8") as f:
        content = f.read()

    assert "Dikshu.png" in content
    assert "Images" in content

def test_log_move_appends_multiple_entries(tmp_path):
    log_path = str(tmp_path/"log.txt")
    fm.log_move("Dikshu.png","Images",log_path)
    fm.log_move("Anmol.py","Code",log_path)

    with open(log_path, "r",encoding="utf-8") as f:
        lines = f.readlines()
    assert len(lines) == 2
    assert "Dikshu.png" in lines[0]
    assert "Anmol.py" in lines[1]

def test_log_move_format(tmp_path):
    log_path = str(tmp_path/"log.txt")
    fm.log_move("Note.txt","TextFiles",log_path)
    with open(log_path, "r",encoding="utf-8") as f:
        content = f.read()
    assert content.startswith("[")
    assert "→" in content
    assert "TextFiles/" in content