"""Functions to write data from the SQL database to csv files and zip them up."""
import csv
import constants as c
from ETL import wrangling_functions as w
import uuid
from filters import filter_SQL_queries as fq
import os
import zipfile
from csv_writer import extractor_SQL_queries as eq


def make_zip_folder(phase_tbl_cols_dict: dict, pids_list):
    """Input: Dictionary of phase name to dictionary of table name to column label list.
    Output: Returns name of the zip folder containing all subjects data from the given columns of the given tables."""
    unique_id = str(uuid.uuid1())
    full_path = c.DOWNLOAD_FILES_PATH + '\\' + unique_id
    try:
        os.mkdir(full_path)
    except OSError:
        print("Creation of the directory %s failed" % full_path)

    make_nodes_data_csv(phase_tbl_cols_dict, pids_list, full_path)
    make_edges_data_csv(phase_tbl_cols_dict, pids_list, full_path)

    zipf = zipfile.ZipFile(full_path + '\\' + c.DOWNLOAD_ZIP_FOLDER_NAME, 'w')  # create zip-handle
    zip_up_files(zipf, full_path)  # zip up the files
    zipf.close()
    #return unique_id + '.zip'  # return the name of the zip folder
    return unique_id + '/' + c.DOWNLOAD_ZIP_FOLDER_NAME  # return the name of the zip folder


def zip_up_files(ziphandle, full_path):
    """Input: Ziphandle object; list of full file name (sub-)selection
    of those files contained in the given file path to zip up.
    Output: Zips up the selection of files and removes the unzipped versions."""
    for root, dirs, files in os.walk(full_path):
        for file in files:
            if file in c.DOWNLOAD_FILE_NAMES_LIST:
                try:
                    ziphandle.write(os.path.join(root, file), file)
                except Exception as e:
                    print("Exception occurred: %s " % e)
    remove_csvs(full_path)


def remove_csvs(full_path):
    for file_name in c.DOWNLOAD_FILE_NAMES_LIST:
        path_and_name = full_path + '\\' + file_name
        if os.path.exists(path_and_name):
            os.remove(path_and_name)
        else:
            print(path_and_name + " deletion was unsuccessful")


def make_nodes_data_csv(phase_tbl_cols_dict, pids_list, full_path):
    """Input: Dictionary of phase name to dictionary of table name to column label list;
    list of pids for which to get the selected data; full path at which to make the csv.
    Output: Creates a csv of the selected data for the selected PIDs."""
    full_data_nodes = eq.get_single_subjects_tbl_of_all_given_tbls_and_cols(phase_tbl_cols_dict, pids_list)
    write_list_to_csv(c.DOWNLOAD_FILE_NAME_NODES, full_data_nodes, full_path)


def make_edges_data_csv(phase_tbl_cols_dict, pids_list, full_path):
    """Input: Dictionary of phase name to dictionary of table name to column label list;
    list of pids for which to get the selected data on shared edges; full path at which to make the csv.
    Output: Creates a csv of the selected data for shared edges of selected PIDs."""
    edges_list = fq.get_full_edge_ids_for_pids_list(pids_list)
    full_data_edges = eq.get_single_edges_tbl_of_all_given_tbls_and_cols(phase_tbl_cols_dict, edges_list)
    write_list_to_csv(c.DOWNLOAD_FILE_NAME_EDGES, full_data_edges, full_path)


def write_list_to_csv(filename: str, data: list, full_path, is_list_of_lists=True):
    """Input: List of data to be written to a csv; filename; full path to the file;
    if data is lists of strings be sure to change the flag.
    Output: Creates a csv of the given data, with each list being a row."""
    filepath = full_path + '\\' + filename
    w.create_empty_csv(filepath)
    with open(filepath, "a", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL, doublequote=True, delimiter=",")
        for row in data:
            if is_list_of_lists:
                writer.writerow(row)
            else:
                writer.writerow([row])
