cd "${INSTALLDIR}/${NAME}/freebasics/"
manage="${VENV}/bin/python ${INSTALLDIR}/${NAME}/freebasics/manage.py"

$manage migrate --settings=freebasics.settings.production

# process static files
$manage compress --settings=freebasics.settings.production
$manage collectstatic --noinput --settings=freebasics.settings.production

# compile i18n strings
$manage compilemessages --settings=freebasics.settings.production
