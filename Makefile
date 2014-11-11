theme/groupon/index.html: theme/groupon/index.html.tmpl theme/fog_donors/ruler-groupon-amount.txt
	theme/fog_donors/render_page.py \
		$$(cat theme/fog_donors/ruler-groupon-amount.txt) \
		<   $<   >   $@
