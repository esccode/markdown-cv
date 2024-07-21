# #!/usr/bin/env python3

# # metadata.py
# # Author: esccode.pl
# # Date: 7/8/2024
# # Metadata

# ## Reading metadata

# from pypdf import PdfReader

# reader = PdfReader("cysa_85_v1_merged.pdf")

# meta = reader.metadata

# print(len(reader.pages))

# ### All of the following could be None!

# print(meta.author)
# print(meta.creator)
# print(meta.producer)
# print(meta.subject)
# print(meta.title)

# ## Writing metadata

from datetime import datetime
# from pypdf import PdfReader, PdfWriter

# reader = PdfReader("cysa_85_v1_merged.pdf")
# writer = PdfWriter()

# ### Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# ### If you want to add the old metadata, include this line
# metadata = reader.metadata
# writer.add_metadata(metadata)

### Format the current date and time for the metadata
utc_time = "-05'00'"  # UTC time optional
time = datetime.now().strftime(f"D\072%Y%m%d%H%M%S{utc_time}")

# ### Add the new metadata
# writer.add_metadata(
#     {
#         "/Author": "esccode.pl",
#         "/Producer": "esccode.pl",
#         "/Title": "Comptia_CySA_cs0-003",
#         "/Subject": "comptia_CySA_cs0-003_85-question",
#         "/Keywords": ["CySA","comptia","cs0-003","security","cybersecurity"],
#         # "/Keywords": "CySA",
#         "/CreationDate": time,
#         "/ModDate": time,
#         # "/Creator": "esccode.pl",
#         # "/CustomField": "esccode.pl",
#     }
# )

# # Save the new PDF to a file
# with open("cysa_85_v1_merged.pdf", "wb") as f:
#     writer.write(f)


# ## Reading metadata

# from pypdf import PdfReader

# reader = PdfReader("cysa_85_v1_merged.pdf")

# meta = reader.metadata

# print(len(reader.pages))

# ### All of the following could be None!

# print(meta.author)
# print(meta.creator)
# print(meta.producer)
# print(meta.subject)
# print(meta.title)


## Updating metadata

from pypdf import PdfReader, PdfWriter

writer = PdfWriter(clone_from="cv_jacek-wieteska.pdf")

### Change some values.
writer.add_metadata(
    {
        "/Author": "esccode.pl",
        # "/Producer": "Libre Writer",
        "/Title": "Resume, IT Security Analyst, ReCREWter",
        # "/Subject": "comptia_CySA_cs0-003_85-sample-question",
        "/Keywords": ["IT Security Analyst","data","analyst","comptia","security","cybersecurity","resume","cv","job"],
        "/CreationDate": time,
        "/ModDate": time,
    }
)

### Save the new PDF to a file
with open("resume_jacek-wieteska_IT-Security-Analyst_ReCREWter.pdf", "wb") as f:
    writer.write(f)