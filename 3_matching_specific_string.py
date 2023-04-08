
import re
Regex_Pattern = r'hackerrank'  # Do not delete 'r'.


Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))


# **************SAMPLE_INPUT*****************

# The hackerrank team is on a mission to flatten the world by restructuring the
# DNA of every company on the planet. We rank programmers based on their coding
# skills, helping companies source great programmers and reduce the time to hire.
# As a result, we are revolutionizing the way companies discover and evaluate 
# talented engineers.The hackerrank platform is the destination for the best 
# engineers to hone their skills and companies to find top engineers.

# ***************OUTPUT******************

# Number of matches: 2


