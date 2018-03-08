$HERE=`pwd`
cd ../simple/bin
unlink bin/pdftotext
ln -s ../../../bin-linux_x64/pdftotext
cd ..
zip -r main.zip *
aws lambda update-function-code --function-name=DEV-pdf-text-extractor --zip-file=fileb://./main.zip
rm main.zip
cd $HERE
