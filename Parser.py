###################################### Import relevant libraries ############################################
import numpy as np
import pandas as pd
import streamlit as st
import pickle
import time
from myClassifier import classif, noBehavior


#############################################################################################################


def Jparse(item=object):

    with st.spinner('We are analyzing your file.....this may take a while!!!'):
        time.sleep(10)

        json_load = item
        with open('classifier/features.pkl', 'rb') as f:
            features = pickle.load(f)

        signature = []
        if json_load.__contains__('signatures'):   # check if behaviour key exists in the dictionary
            signatures = json_load['signatures']

        for signature_length in range(1, len(signatures)):
            if signatures[signature_length].__contains__('description'):
                tempp = signatures[signature_length]
                des = tempp['description']
                signature.append(des)

    ################################ Extract the behavior and strings dictionary ################################
        sample_buffer = []
        if json_load.__contains__('behavior'):  # check if behaviour key exists in the dictionary
            behavior = json_load['behavior']

        ####################################### Extract the generic, apistats and summary lists #####################
            if behavior.__contains__('generic'):  # Check if generic key exists in dictionary
                generic = behavior['generic']
            else:
                print("The generic key is missing from the report, please check report!!")

            if behavior.__contains__('apistats'):  # Check if apistats key exists in dictionary
                apistats = behavior['apistats']
            else:
                print("The API stats are missing from the report, please check report!!")

            if behavior.__contains__('summary'):  # Check if summary key exists in dictionary
                summary = behavior['summary']
            else:
                print("The summery for the behavioral analysis is missing from the report, please check report!!")

            ##############################################################################################################

            ###################################### Extract process IDs from the generic list #############################

            size = len(generic)                            #get size of generic to set size of array
            process_IDs = np.empty(size, dtype=object)     # create empty array with size equal to generic

            for a in range(size):
                process = generic[a]
                process_IDs[a] = process['pid']

            #############################################################################################################

            ############################################## Extract APIs list ###########################################

            for b in process_IDs:
                buf = str(b)
                if apistats.__contains__(buf):
                    temp = apistats[buf]
                    for d in temp:
                        sample_buffer.append(d)

                APIs = list(dict.fromkeys(sample_buffer))

            ##################################### Extract RegKey features from the summery dictionary ##########################
            sample_buffer1 = []
            if summary.__contains__('regkey_deleted'):
                RegDeleted = summary['regkey_deleted']

                for bb in RegDeleted:
                    sample_buffer1.append(bb)

            ##################################################

            if summary.__contains__('regkey_opened'):
                RegOpened = summary['regkey_opened']

                for bb in RegOpened:
                    sample_buffer1.append(bb)
            #####################################################

            if summary.__contains__('regkey_read'):
                RegRead = summary['regkey_read']

            for bb in RegRead:
                sample_buffer1.append(bb)

            ##########################################################
            if summary.__contains__('regkey_written'):
                RegWritten = summary['regkey_written']

                for bb in RegWritten:
                    sample_buffer1.append(bb)

            ##################################### Extract file operation features from the summery dictionary ##########################
            if summary.__contains__('file_deleted'):
                File_Deleted = summary['file_deleted']

                for bb in File_Deleted:
                    sample_buffer1.append(bb)

            ##################################################

            if summary.__contains__('file_opened'):
                File_Opened = summary['file_opened']

                for bb in File_Opened:
                    sample_buffer1.append(bb)

            #####################################################

            if summary.__contains__('file_read'):
                file_Read = summary['file_read']

                for bb in file_Read:
                    sample_buffer1.append(bb)

            ##########################################################
            if summary.__contains__('file_written'):
                file_Written = summary['file_written']

                for bb in file_Written:
                    sample_buffer1.append(bb)

            ################################### Extract directory operations directory_enumerated
            if summary.__contains__('directory_created'):
                directory_created = summary['directory_created']

                for bb in directory_created:
                    sample_buffer1.append(bb)

            ######################################################

            if summary.__contains__('directory_enumerated'):
                directory_enumerated = summary['directory_enumerated']

                for bb in directory_enumerated:
                    sample_buffer1.append(bb)

            if json_load.__contains__('strings'):  # Check if strings key exists in dictionary
                strings = json_load['strings']

                for bb in strings:
                    sample_buffer1.append(bb)

            ######################################################
            sss = APIs+sample_buffer1
            ss = []
            for x in features:
                if x in sss:
                    ss.append(1)
                else:
                    ss.append(0)

                ################## Convert sample array to dataframe#################
            sample_ = pd.DataFrame(ss)
            sample = sample_.transpose()
            st.success('Done!')
            classif(signature, sample)
        else:
            st.write("The dynamic analysis is missing from the report, please check the report!! \n")
            st.write("Making analysis based on signatures......... \n")
            st.success('Done!')
            noBehavior(signature)




