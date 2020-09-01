## dataset in datasets/testcase

- combine the data into a file from testcase/
```
combine.py
```

- transfer the file to adapt to gpt-2
```
cd datasets
transfer.py {in.txt} {transfer_out.txt}
```

- learn bpe
```
python subword_nmt\learn_bpe.py -o {outFile.bpe} -i {inFile} --symbols 50000 --min-frequency  2
```

- to encoder.json
```
python to_json {inFile.bpe} {outFile.json}
```