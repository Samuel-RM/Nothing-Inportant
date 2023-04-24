#Whit this progr
def main(first_list):
    output = []

    for each_word in first_list:
        if type(each_word) == bool:
            print(f"I don't accpet {each_word} in my list, sorry .")
        else:
            try:
                assert type(each_word) == str, f"{each_word} is not a string"
                assert len(each_word) == 0 , f"I don't want empty str"
                output.append(each_word[2])
            except AssertionError as err:
                print(err) 
    return output


first_list = [2, 'tucan', True, 5.04, 'Guacamaya']
print('\nThe results of the function was:' , main(first_list))
