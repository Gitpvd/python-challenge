{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "pypollfile_path=\"election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3521001\n"
     ]
    }
   ],
   "source": [
    "with open(\"election_data.csv\",\"r\") as pypollfile:\n",
    "     csv_reader = csv.reader(pypollfile, delimiter=',') \n",
    "     row_count = sum(1 for row in csv_reader) \n",
    "     all_votes = row_count-1\n",
    "     print(all_votes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "ids=[]\n",
    "county=[]\n",
    "candidate=[]\n",
    "election={\"ids\",\"county\",\"candidate\"}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Khan\n"
     ]
    }
   ],
   "source": [
    "candidate=[]\n",
    "canvalue= str\n",
    "with open(\"election_data.csv\",\"r\") as pypollfile:\n",
    "    csv_reader = csv.DictReader(pypollfile,delimiter=',')\n",
    "    for row in csv_reader:\n",
    "        canvalue= row['Candidate']\n",
    "        candidate.append(canvalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16793141\n"
     ]
    }
   ],
   "source": [
    "idvalue= int\n",
    "with open(\"election_data.csv\",\"r\") as pypollfile:\n",
    "    csv_reader = csv.DictReader(pypollfile,delimiter=',')\n",
    "    for row in csv_reader:\n",
    "        idvalue= row['Voter ID']\n",
    "        ids.append(idvalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marsh\n"
     ]
    }
   ],
   "source": [
    "countyvalue= int\n",
    "with open(\"election_data.csv\",\"r\") as pypollfile:\n",
    "    csv_reader = csv.DictReader(pypollfile,delimiter=',')\n",
    "    for row in csv_reader:\n",
    "        countyvalue= row['County']\n",
    "        county.append(countyvalue)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Correy', \"O'Tooley\", 'Khan', 'Li']\n"
     ]
    }
   ],
   "source": [
    "candidate_list=list(set(candidate))\n",
    "print(candidate_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'dict' object has no attribute 'append'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-59-188c4af04af6>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0melection_results\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 14\u001b[0;31m \u001b[0melection_results\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mcandidate_list\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     15\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0melection_results\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'dict' object has no attribute 'append'"
     ]
    }
   ],
   "source": [
    "#Get total votes for each candidate\n",
    "correy_votes=candidate.count(\"Correy\")\n",
    "otooley_votes=candidate.count(\"O'Tooley\")\n",
    "khan_votes=candidate.count(\"Khan\")\n",
    "li_votes=candidate.count(\"Li\")\n",
    "\n",
    "#Get % of total vote each candidate got\n",
    "per_correy=((correy_votes/all_votes)*100)\n",
    "per_otooley=((otooley_votes/all_votes)*100)\n",
    "per_khan=((khan_votes/all_votes)*100)\n",
    "per_li=((li_votes/all_votes)*100)\n",
    "\n",
    "election_results={}\n",
    "election_results.append[candidate_list]\n",
    "print(election_results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open(\"output2.txt\",\"a\")\n",
    "print(\"Election Results \\n----------------------------------\",file=f) \n",
    "print(\"Total votes: %s\" %all_votes,file=f) \n",
    "print(\"\\n----------------------------------\",file=f)\n",
    "print(candidate_list[0],\":\",per_correy,\"%\", \"(\", correy_votes,\")\",file=f)\n",
    "print(candidate_list[0],\":\",per_correy,\"%\", \"(\", correy_votes,\")\",file=f)\n",
    "print(candidate_list[1],\":\",per_otooley,\"%\", \"(\", otooley_votes,\")\",file=f)\n",
    "print(candidate_list[2],\":\",per_khan,\"%\", \"(\", khan_votes,\")\",file=f)\n",
    "print(candidate_list[3],\":\",per_li,\"%\", \"(\", li_votes,\")\",file=f)\n",
    "print(\"----------------------------------\",file=f)\n",
    "print(\"Winner: %s\" ,file=f) \n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results \n",
      "----------------------------------\n",
      "Total votes: 3521001\n",
      "----------------------------------\n",
      "Correy : 19.999994319797125 % ( 704200 )\n",
      "O'Tooley : 2.999999147969569 % ( 105630 )\n",
      "Khan : 63.00001050837531 % ( 2218231 )\n",
      "Li : 13.999996023857989 % ( 492940 )\n",
      "----------------------------------\n"
     ]
    }
   ],
   "source": [
    "print(\"Election Results \\n----------------------------------\") \n",
    "print(\"Total votes: %s\" %all_votes) \n",
    "print(\"----------------------------------\")\n",
    "print(candidate_list[0],\":\",per_correy,\"%\", \"(\", correy_votes,\")\")\n",
    "print(candidate_list[1],\":\",per_otooley,\"%\", \"(\", otooley_votes,\")\")\n",
    "print(candidate_list[2],\":\",per_khan,\"%\", \"(\", khan_votes,\")\")\n",
    "print(candidate_list[3],\":\",per_li,\"%\", \"(\", li_votes,\")\")\n",
    "print(\"----------------------------------\")\n",
    "print(\"Winner: %s\": )\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
