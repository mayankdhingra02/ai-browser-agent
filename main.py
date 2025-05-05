from browser_control import take_screenshot, click_at
from gpt_agent import ask_gpt
from utils import image_to_base64

def main():
    screenshot_path = take_screenshot()
    image_data = image_to_base64(screenshot_path)

    # Get GPT's suggestion
    response = ask_gpt(screenshot_base64=image_data, prompt="Tell me where to click to sign in on this page")

    print("[GPT Suggestion]")
    print(response)

    # Optionally: extract and execute coordinates from GPT response
    # click_at(x, y)

if __name__ == "__main__":
    main()
