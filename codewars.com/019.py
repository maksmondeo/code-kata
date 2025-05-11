"""
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    l = ["https://", "http://", "https://www.", "www."]
    for i in l:
        if i in url:
            url = url.replace(i, "")

    result = ""
    l = list(url)
    for i in l:
        if i == ".":
            return result
        else:
            result += i
