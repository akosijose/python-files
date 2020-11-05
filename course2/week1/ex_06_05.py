text = "X-DSPAM-Confidence:    0.8475";
find_text = text.find(":")
slice_text = text[find_text+5:]
value = float(slice_text)
print(value)