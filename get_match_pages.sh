for match_id in 1006074 1006054 1006090 1006113 
do
  curl https://www.whoscored.com/Matches/${match_id}/Live > original_pages/page_${match_id}
done
