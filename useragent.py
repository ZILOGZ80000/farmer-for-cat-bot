import random

def rand():
    browsers = [
        "Chrome",
        "Firefox",
        "Edge",
        "Opera",
        "Safari"
    ]
    os_list = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 10.0; WOW64",
        "Macintosh; Intel Mac OS X 10_15_7",
        "X11; Linux x86_64",
        "Linux; Android 13; SM-G991B",
        "iPhone; CPU iPhone OS 17_0 like Mac OS X"
    ]
    browser = random.choice(browsers)
    os_str = random.choice(os_list)

    if browser == "Chrome":
        major = random.randint(110, 130)
        minor = random.randint(0, 0)
        build = random.randint(5000, 7000)
        patch = random.randint(0, 199)
        ua = f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{major}.0.{build}.{patch} Safari/537.36"
    elif browser == "Firefox":
        major = random.randint(100, 130)
        ua = f"Mozilla/5.0 ({os_str}; rv:{major}.0) Gecko/20100101 Firefox/{major}.0"
    elif browser == "Edge":
        major = random.randint(110, 130)
        build = random.randint(2000, 3000)
        patch = random.randint(0, 199)
        ua = f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{major}.0.0.0 Safari/537.36 Edg/{major}.0.{build}.{patch}"
    elif browser == "Opera":
        major = random.randint(90, 110)
        build = random.randint(4000, 7000)
        patch = random.randint(0, 199)
        ua = f"Mozilla/5.0 ({os_str}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{major}.0.{build}.{patch} Safari/537.36 OPR/{major}.0.{build}.{patch}"
    elif browser == "Safari":
        major = random.randint(14, 17)
        minor = random.randint(0, 5)
        webkit = random.randint(600, 610)
        ua = f"Mozilla/5.0 ({os_str}) AppleWebKit/{webkit}.1.15 (KHTML, like Gecko) Version/{major}.{minor} Safari/{webkit}.1.15"
    else:
        ua = "Mozilla/5.0"

    return ua