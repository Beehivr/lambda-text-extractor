ARG1=$1

HERE=`pwd`
APP_ROOT=$HERE/../simple

FCT_NAME='pdf-text-extractor'


function prepare_package() {
  cd $APP_ROOT/bin
  unlink pdftotext
  ln -s ../../../bin-linux_x64/pdftotext
  cd $APP_ROOT
  zip -r main.zip *
}

function copy_package() {
  cd $APP_ROOT
  echo ""
  echo "deploying to λ function $1"
  aws lambda update-function-code --function-name=$1 --zip-file=fileb://main.zip
}

if [ -z $ARG1 ]; then
  echo 'usage: deploy.sh [dev|qa|staging|production|test] [test]'
  exit 1;
fi

if [ $ARG1 = 'dev' ]; then
  echo 'deploying to dev'
  prepare_package
  copy_package 'DEV-pdf-text-extractor'
fi

if [ $ARG1 = 'qa' ]; then
  echo 'deploying to qa'
  prepare_package
  copy_package 'QA-pdf-text-extractor'
fi

if [ $ARG1 = 'staging' ]; then
  echo 'deploying to staging'
  prepare_package
  copy_package 'STG-pdf-text-extractor'
fi

if [ $ARG1 = 'production' ]; then
  echo 'deploying to production'
  prepare_package
  copy_package 'PROD-pdf-text-extractor'
fi

cd $APP_ROOT
rm main.zip

cd $HERE

echo 'done'
