#!/bin/bash

# Location to place backups.
BACKUP_DIR="/mnt/odoo/backup"


# Location of the backup logfile.
LOGFILE="$BACKUP_DIR/logfile.log"
touch $LOGFILE

user=odoo
timeslot=`date +%d%m%y%H%M%S`
databases=`psql -U $user -q -c "\l" | awk '{ print $1}' | grep -vE '^\||^-|^List|^Name|template[0|1]|^\('`

for i in $databases; do
    timeinfo=`date '+%T %x'`
    echo "Backup and Vacuum started at $timeinfo for time slot $timeslot on database: $i " >> $LOGFILE
    /usr/bin/vacuumdb -z -U $user $i >/dev/null 2>&1
    /usr/bin/pg_dump $i -U $user | gzip > "$BACKUP_DIR/$i-$timeslot-db.gz"
    timeinfo=`date '+%T %x'`
    echo "Backup and Vacuum complete at $timeinfo for time slot $timeslot on database: $i " >> $LOGFILE
done

 #-------------------------------------------------

 # delete files more than 10 days old
 find $BACKUP_DIR/* -mtime +10 -exec rm {} \;
