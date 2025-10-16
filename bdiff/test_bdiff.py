import bdiff
import os

def test_bdiff():
    base_diff_path = "../diff-cases/"
    left_files = sorted(os.listdir(base_diff_path + r"left_files"))
    right_files = sorted(os.listdir(base_diff_path + r"right_files"))
    with open("../diff-cases/edit_scripts", 'r', encoding="utf8") as es_file:
        edit_scripts = eval(es_file.read())
    for left_file, right_file, expected_es in zip(left_files, right_files, list(edit_scripts.values())):
        print(left_file)
        computed_es = bdiff.bdiff(base_diff_path + r"left_files/" + left_file, base_diff_path + r"right_files/" + right_file)
        assert computed_es == expected_es, left_file + ": " + str(computed_es)