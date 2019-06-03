from google import google
import os
import requests


class acquire_catlalog():
    def __init__(self, source_file, output_folder, num_page = 1):
        self.source_file_ = source_file
        self.output_folder_ = output_folder
        self.num_page_ = num_page

    def parse_source_file(self):
        if ("txt" not in self.source_file_.split(".")[-1] ):
            raise Exception("Source file should be txt format")
        with open(self.source_file_, "r") as file:
            self.item_list_ = file.read().splitlines()
            print(self.item_list_)
        return self.item_list_

    def google_search_pdf(self, dictionary_list):
        self.output_dict_ = {}
        i = 1
        for keyword in dictionary_list:
            keyword_ = keyword + " filetype:pdf"
            print("{0} : Google Searching Keyword: {1}".format(i, keyword_))
            self.output_dict_[str(keyword)] = google.search(keyword_, self.num_page_)
            print(self.output_dict_[str(keyword)])
            i += 1
        return self.output_dict_

    def download_pdf(self, output_dict):
        if not os.path.isdir(self.output_folder_):
            os.mkdir(self.output_folder_)

        for key, values in output_dict.items():
            num_download = 3 if values.__len__() >= 3 else values.__len__()
            print("Search keyword: {0}".format(key))
            print( 100* "=")
            for i in range(num_download):
                try:
                    pdf_link = values[i].link
                    pdf_name = pdf_link.split("/")[-1] if "=" not in pdf_link.split("/")[-1] else str(i)
                    print("Downloading {0},  link: {1}".format(pdf_name, pdf_link))
                    if ".pdf" in pdf_link
					
                        response = requests.get(pdf_link, stream = True)
						total_length = response.headers.get('content-length')
                        if not os.path.isdir(key):
                            key = key.replace("/", "_").replace("\t", " ")
                            os.mkdir(key)
                        with open("./" + key + "/" + pdf_name + ".pdf", "wb") as file:
                            if total_length is None: # no content length header
								f.write(response.content)
							else:
								dl = 0
								total_length = int(total_length)
								for data in response.iter_content(chunk_size=4096):
									dl += len(data)
									f.write(data)
									done = int(50 * dl / total_length)
									sys.stdout.write("\r[%s%s] %s %" % ('=' * done, ' ' * (50-done), str(2*done)) )    
									sys.stdout.flush()
				except:
					pass
						print(100 * "-")
			
		import requests

with open(file_name, "wb") as f:
        print "Downloading %s" % file_name
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        
			
			
if __name__ == "__main__":
    a = acquire_catlalog("search_list.txt", "TOA_test")
    a.parse_source_file()
    a.google_search_pdf(a.item_list_)
    a.download_pdf(a.output_dict_)