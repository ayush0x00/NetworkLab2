
import subprocess
resources = ["https://cloud.iitmandi.ac.in/f/36c1c10b5caf46948ee9/?dl=1",
             "https://cloud.iitmandi.ac.in/f/fef3ed77ad16482582f9/?dl=1",
             "https://cloud.iitmandi.ac.in/f/f760934703f647c49dbb/?dl=1",
             "https://cloud.iitmandi.ac.in/f/5d31e8769b954109be61/?dl=1",
             "https://cloud.iitmandi.ac.in/f/0e1dfdb780e845129513/?dl=1",
             "https://cloud.iitmandi.ac.in/f/07109a50545d4930a714/?dl=1",
             "https://cloud.iitmandi.ac.in/f/2984f340696b4ab8b301/?dl=1",
             "https://cloud.iitmandi.ac.in/f/c200476d3ce247e08c87/?dl=1",
             "https://cloud.iitmandi.ac.in/f/d276f3cbe766409db927/?dl=1"
             ]


def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True,
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        return (std_out.strip(), std_err)
    pass

# runcmd(f'wget {resources[3]} -O/dev/null 2>&1 | grep -o "[0-9.]\+ [KM]*B/s" ', verbose = True)
def downloadFile(fileName):
    for idx,url in enumerate(resources):
        with open(fileName,"a") as file:
            file.write(f"Results for resource {idx+1}\n")
            for loop in range(5):
                res = runcmd(f'wget {url} -O/dev/null 2>&1 | grep -o "[0-9.]\+ [KM]*B/s" ', verbose = True)
                if(res[1]):
                    print(f'Error occurred======{res[1]}')
                else:
                    file.write(f"Loop {loop+1} throughput {res[0]}\n")

def downloadWithLimit(fileName,limit):
    for idx,url in enumerate(resources):
        with open(fileName,"a") as file:
            file.write(f"Results for resource {idx+1} with limit {limit}\n")
            for loop in range(5):
                res = runcmd(f'wget {url} -O/dev/null --limit-rate {limit} 2>&1 | grep -o "[0-9.]\+ [KM]*B/s" ', verbose = True)
                if(res[1]):
                    print(f'Error occurred======{res[1]}')
                else:
                    file.write(f"Loop {loop+1} throughput {res[0]}\n")

def downloadConcurrent(numberOfDownloads):
    res = runcmd(f'cat resources.txt | xargs -n -1 -P ${numberOfDownloads} wget -O/dev/null 2>&1 | grep -o "[0-9.]\+ [KM]*B/s" ',verbose=True)
    if res[1]:
        print(f"Some error occured for {numberOfDownloads}\n")
        return
    with open("concurrent.txt","a") as file:
        print(f'Result for {numberOfDownloads}\n')
        print(res)
        file.write(f"Result for {numberOfDownloads} concurrent downloads\n")
        file.writelines(res[0]+"\n")


if __name__=="__main__":
    # concurrent = [11,13,14,17,25]
    # for d in concurrent:
    #     downloadConcurrent(d)
    limits = ["1m","2m","3m"]
    for l in limits:
        downloadWithLimit("limit.txt",l)
