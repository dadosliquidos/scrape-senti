import pandas as pd


class Normalization_comments:
    def __init__(self):
        pass

    @classmethod
    def normalization_comment(cls,list_comment: list):
        new_list = []
        for comment in list_comment:
            new_list.append(f'\ '+comment.replace('"',"'")+f' \ ')
        
        return new_list