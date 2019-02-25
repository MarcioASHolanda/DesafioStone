
import re



s = "how much for the maple syrup? $20.99? That's ridiculous!!!"
print(re.sub(r'[^\w]', ' ', s))
# 'how much for the maple syrup   20 99  That s ridiculous   '









