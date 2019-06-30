{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "pypollfile_path=\"election_data.csv\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
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
   "execution_count": 138,
   "metadata": {},
   "outputs": [],
   "source": [
    "ids=[]\n",
    "county=[]\n",
    "candidate=[]\n",
    "election={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [],
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
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
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
   "execution_count": 141,
   "metadata": {},
   "outputs": [],
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
   "execution_count": 186,
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
    "candidate_list=[]\n",
    "candidate_list=list(set(candidate))\n",
    "print(candidate_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[19.999994319797125, 2.999999147969569, 63.00001050837531, 13.999996023857989]\n",
      "{'Correy': 19.999994319797125, \"O'Tooley\": 2.999999147969569, 'Khan': 63.00001050837531, 'Li': 13.999996023857989}\n",
      "Khan\n"
     ]
    }
   ],
   "source": [
    "candidate_list=[]\n",
    "candidate_list=list(set(candidate))\n",
    "\n",
    "#Get total votes for each candidate\n",
    "correy_votes=candidate.count(\"Correy\")\n",
    "otooley_votes=candidate.count(\"O'Tooley\")\n",
    "khan_votes=candidate.count(\"Khan\")\n",
    "li_votes=candidate.count(\"Li\")\n",
    "\n",
    "#Get % of total vote each candidate got\n",
    "vote_per=[]\n",
    "per_correy=((correy_votes/all_votes)*100)\n",
    "vote_per.append(per_correy)\n",
    "per_otooley=((otooley_votes/all_votes)*100)\n",
    "vote_per.append(per_otooley)\n",
    "per_khan=((khan_votes/all_votes)*100)\n",
    "vote_per.append(per_khan)\n",
    "per_li=((li_votes/all_votes)*100)\n",
    "vote_per.append(per_li)\n",
    "print(vote_per)\n",
    "\n",
    "winner=max(vote_per)\n",
    "\n",
    "election_results={\n",
    "    candidate_list[0]:vote_per[0],\n",
    "    candidate_list[1]:vote_per[1],\n",
    "    candidate_list[2]:vote_per[2],\n",
    "    candidate_list[3]:vote_per[3]\n",
    "}\n",
    "print(election_results)\n",
    "i=0\n",
    "for x,y in election_results.items():\n",
    "    while i <= 3:\n",
    "        if  winner == y:\n",
    "            winner_name = x\n",
    "        i += 1\n",
    "print(winner_name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "f=open(\"output2.txt\",\"a\")\n",
    "print((\"Election Results \\n----------------------------------\"),file=f) \n",
    "print(\"Total votes: %s\" %all_votes,file=f) \n",
    "print(\"\\n----------------------------------\",file=f)\n",
    "print((candidate_list[0],\":\",per_correy,\"%\", \"(\", correy_votes,\")\"),file=f)\n",
    "print((candidate_list[1],\":\",per_otooley,\"%\", \"(\", otooley_votes,\")\"),file=f)\n",
    "print((candidate_list[2],\":\",per_khan,\"%\", \"(\", khan_votes,\")\"),file=f)\n",
    "print((candidate_list[3],\":\",per_li,\"%\", \"(\", li_votes,\")\"),file=f)\n",
    "print(\"----------------------------------\",file=f)\n",
    "print((\"Winner: \",winner_name),file=f) \n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
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
      "----------------------------------\n",
      "Winner:  Khan\n"
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
    "print(\"Winner: \",winner_name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
