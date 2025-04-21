'''
1. INPUT TOTAL NUMBER OF SITES:
   - We start by taking the total number of distributed processes/sites in the system.

2. GENERATE REQUEST SET FOR EACH SITE:
   - For each site `i`, we build a list of all other sites (excluding itself).
   - This list represents the sites to which `i` must send a request message whenever it wants to enter the critical section (CS).
   - This is stored in a dictionary `request_set` where key = site number, value = list of other site numbers.

3. INPUT NUMBER OF SITES REQUESTING CS ACCESS:
   - We then ask how many sites want to enter the critical section.
   - For each requesting site, we take a tuple input: (timestamp, site number).
   - This captures the moment at which the request was made.

4. SORT THE REQUESTS:
   - We sort all the (timestamp, site) tuples in ascending order of timestamp.
   - This determines the priority of CS access (lower timestamp gets preference).

5. SENDING REQUEST MESSAGES:
   - Each site that wants to access the CS sends a request message to all the sites in its request set (i.e., all other sites).
   - This is printed out for visualization.

6. BUILD A LIST OF REQUESTING SITES:
   - We maintain a list of site numbers that have requested access.
   - This helps in checking whether a given site is currently competing for CS.

7. HANDLING REPLIES AND ACCESS TO CS:
   - For each requesting site (in timestamp order):
     a. We loop through all other sites in its request set.
     b. If the other site is NOT requesting CS:
        - It immediately sends a REPLY message back.
     c. If the other site IS ALSO requesting CS:
        - We compare timestamps.
        - If the current site has an earlier timestamp, the other site will send a REPLY message.
        - If the current site has a later timestamp, the other site withholds the reply (this is effectively a denial/delay).
        - This denial is now printed as a message like "Site X is not sending reply to Site Y yet".

8. ENTERING CRITICAL SECTION:
   - Once a site receives reply messages from all members of its request set, it is allowed to enter the CS.
   - This is printed for clarity.

9. EXITING CRITICAL SECTION:
   - After executing in CS, the site "exits" and is removed from the `request_site` list.
   - This signifies it can now start replying to others (which were previously denied).

10. LOOP CONTINUES UNTIL ALL REQUESTING SITES HAVE BEEN GRANTED ACCESS ONE-BY-ONE BASED ON TIMESTAMP ORDER.

Key Concept:
- Denial in Ricart-Agrawala is not permanent — it’s a delay based on timestamp priority.
- No central coordinator is involved; mutual exclusion is achieved through request/reply messages and logical clocks.
'''

'''
1. TOTAL SITES INPUT KARNA:
   - Sabse pehle user se poochha jaata hai ki system me total kitne sites/processes hain.

2. REQUEST SET BANANA:
   - Har site ke liye ek list banayi jaati hai jisme baaki saare sites hote hain (khud ko chhodke).
   - Ye list dikhati hai ki jab site CS (Critical Section) me jaana chahegi to kin sites ko request bhejna hoga.
   - Dictionary me store kiya jaata hai: `{ site_no : [baaki sites] }`.

3. KAUN-KAUN SI SITES CS MAANG RAHI HAIN:
   - Phir input liya jaata hai ki kitni sites CS me jaana chahti hain.
   - Har requesting site se timestamp aur site number input liya jaata hai.
   - Timestamp ye dikhata hai ki kis time par request bheji gayi thi.

4. REQUESTS KO SORT KARNA:
   - Sabhi (timestamp, site) pairs ko timestamp ke basis par chhote se bade order me sort karte hain.
   - Ye priority define karta hai ki pehle kaun CS me jaayega.

5. REQUEST MESSAGES PRINT KARNA:
   - Har requesting site apne request set me jo sites hain unko request message bhejti hai.
   - Ye step print statements se dikhaya jaata hai.

6. REQUEST KAR RAHI SITES KI LIST:
   - Ek list banate hain jisme sabhi CS maang rahi sites ke number hote hain.
   - Isse check karne me help milti hai ki koi site request kar rahi hai ya nahi.

7. REPLIES AUR CS ACCESS KA LOGIC:
   - Har requesting site ke liye:
     a. Uske request set ke har site ko check karte hain.
     b. Agar dusri site CS nahi maang rahi:
        - Turant reply bhej diya jaata hai.
     c. Agar dono sites CS maang rahi hain:
        - Timestamps compare kiye jaate hain.
        - Agar current site ka timestamp chhota hai to dusri site reply bhejti hai.
        - Agar current site ka timestamp bada hai to dusri site reply nahi bhejti (ye delay/denial hota hai).
        - Ab code me ye denial explicitly print hota hai — "Site X is not sending reply to Site Y yet".

8. CS ME ENTER KARNA:
   - Jab kisi site ko apne request set ki sabhi sites se reply mil jaata hai, tab wo CS me enter kar sakti hai.
   - Ye step clearly print kiya jaata hai.

9. CS SE EXIT KARNA:
   - CS me kaam karke site exit karti hai aur usse requesting list se hata diya jaata hai.
   - Ab wo site dusri pending sites ko reply bhej sakti hai.

10. YE PROCESS TAB TAK CHALTI HAI JAB TAK SAARI REQUESTING SITES EK-EK KARKAR CS ME NAHIN JAATI.
'''



n = int(input("Enter no. of sites: "))

request_set = {}

# Create request set for each site (all other sites)
for i in range(1, n+1):
    lst = []
    for j in range(1, n+1):
        if i != j:
            lst.append(j)
    request_set[i] = lst

n = int(input("Enter no. of sites who want to enter the CS: "))

request_sites = []

# Get timestamp and site number of sites requesting CS
for i in range(n):
    tupl = [int(x) for x in input("Enter the timestamp and site no. : ").split()]
    request_sites.append(tuple(tupl))

print()

# Sort requests by timestamp
request_sites = sorted(request_sites)

# Each requesting site sends request message to others in its request set
for i in request_sites:
    for j in request_set[i[1]]:
        print("Site {} sending request message to site {}".format(i[1], j))

print()

request_site = []

# List of sites requesting CS
for i in request_sites:
    request_site.append(i[1])

# Handle replies and CS entry
for tupl in request_sites:
    cur_req_site = tupl[1]  # current requesting site

    for i in request_set[cur_req_site]:
        if i not in request_site:
            # site i is not requesting CS, it sends reply
            print("Site {} sending reply message to site {}".format(i, cur_req_site))
        else:
            # both are requesting CS, compare timestamps
            for j in request_sites:
                if i == j[1]:
                    if j[0] > tupl[0]:
                        print("Site {} sending reply message to site {}".format(i, cur_req_site))
                    else:
                        print("Site {} is not sending reply to site {} yet (waiting for its own CS access)".format(i, cur_req_site))

    print("\nSince Site {} has received reply messages from all sites in its request set, therefore it enters the CS".format(cur_req_site))

    if len(request_site) > 0:
        print("\nSite {} exits the CS\n".format(cur_req_site))

    request_site.pop(0)
