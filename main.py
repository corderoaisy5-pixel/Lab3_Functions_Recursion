import access_control as ac 
import media_engine as me

CONTROL_NUM = 4  # Must be an int
FAVORITE_ARTIST = "THE 1975"
ARTIST_LEN = len(FAVORITE_ARTIST)

def signal_decorator(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper 

@signal_decorator 
def signal_shutdown(power, count=0): 
    if power <= 0:
        return count
    print(f"Current signal strength: {power}") # Added 'f'
    return signal_shutdown(power - 1, count + 1) 

def run_exercises():
    # ... (Exercise 1)
    
    print(f"--- Exercise 2: Recursive Signal Shutdown ---")
    initial_power = CONTROL_NUM + ARTIST_LEN 
    total_calls = signal_shutdown(initial_power) 
    print(f"Total recursive calls: {total_calls}\n")
    
    # ... (Exercise 3)

# Don't forget to actually call the function!
if __name__ == "__main__":
    run_exercises()