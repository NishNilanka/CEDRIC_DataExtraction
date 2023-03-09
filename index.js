var tables = null;
$.ajax({
    'async': false,
    'global': false,
    'url': "data.json",
    'dataType': "json",
    'success': function (data) {
        tables = data;
    }
});

$(document).ready(function(){
    let selectValues = [];
    //You can insert api data into this array with the below order. 
    //***** important! Don't change the order. *********

    //generate the table checkboxes code
    let tableList ="";
    for (let i = 0; i < tables.length; i++) {  
        tableList =tableList+
        `
        <li>
        <input type="checkbox" class="tables" id=${i}>
        <label for="${i}">${tables[i][0]}</label>
        </li> 
        `;
    };
    //add the code into wrapper div
    $(".tableListWrap").html(tableList);

    //detect checkbox selections
    $('.tables').change(function() {
        //if checkbox is checked
        if ($(this).is(':checked')) {
            //get the id of the checked checkbox
            let id = parseInt(this.id);
            //get the table's data from the array
            let table = tables[id];

            //generate code
            let code = `
            <h3>Select</h3>
            <h3>Attributes</h3>
            <h3>Data type</h3>
            <h3>DSensitivity</h3>
            <h3>FilterRule</h3>
            `
            for(let i=1; i <table.length; i++){
                code = code +`
                <li>
                <input type="checkbox" class="selectedData" id="${id}-${i}">
                </li>
                <li>
                    ${table[i].attribute}
                </li>
                <li>
                    ${table[i].dataType}
                </li>
                <li>
                    ${table[i].dSensitivity}
                </li>
                <li>
                    ${table[i].filterRule}
                </li>
                `
            }
            $(".tableLDetailsWrap").html(code);

            //select table checkboxes
            let checkboxes = $('.tables');
            //disable other checkboxes
            for (let m = 0; m < checkboxes.length; m++) {
                if(id != checkboxes[m].id){
                    checkboxes[m].disabled =  true;
                };
            };
            //show table attributes table
            $(".tableDetailsMain").removeClass("hide");
        } else {//if checkbox is unchecked
            let checkboxes = $('.tables');
            //enable and remove the check mark of the checkboxes
            for (let m = 0; m < checkboxes.length; m++) {
                    checkboxes[m].disabled = false;
                    checkboxes[m].checked = false;
            };
            //hide and reset the attribute table
            $(".tableDetailsMain").addClass("hide");
            $(".tableLDetailsWrap").html("");
        }
    });

    //show selected values to a table
    $("#selectButton").click(function(){
        let checkboxes = $('.selectedData');
        //assign table and the attribute id to an array using checkbox id
        let tableValue = checkboxes[0].id.split("-");
        let newTable = [];
        //identify checked checkboxes and add those data into an array
        for(i=0; i<checkboxes.length; i++){
            if(checkboxes[i].checked){
                let tableData = checkboxes[i].id.split("-");
                newTable.push(tables[tableData[0]][tableData[1]]);
            }else{
            };
        }
        //add newly created data into the selected value data array
        selectValues.push([tables[tableValue[0]][0],newTable]);
        console.log(selectValues);
        let code = `
        <h3>Table</h3>
        <h3>Attributes</h3>
        <h3>Data type</h3>
        <h3>DSensitivity</h3>
        <h3>FilterRule</h3>
        `
        //generate selected values table
        for(m=0; m < selectValues.length; m++){
            for(let i=0; i <selectValues[m][1].length; i++){
                let rowData = selectValues[m][1];
                if(i == 0 ){
                    code = code +`
                    <li>
                    ${selectValues[m][0]}
                    </li>
                    `
                }else{
                    code = code +`<li></li>`
                }
                code = code +`
                <li>
                    ${rowData[i].attribute}
                </li>
                <li>
                    ${rowData[i].dataType}
                </li>
                <li>
                    ${rowData[i].dSensitivity}
                </li>
                <li>
                    ${rowData[i].filterRule}
                </li>
                `
            };
            code = code +`<hr><hr><hr><hr><hr>`
        };
        let tableCheckboxes = $('.tables');
        for (let m = 0; m < tableCheckboxes.length; m++) {
                tableCheckboxes[m].disabled =  false;
                tableCheckboxes[m].checked = false;
        };
        $(".tableDetailsMain").addClass("hide")
        $(".tableLDetailsWrap").html("");
        $(".sTableLDetailsWrap").html(code);
        $(".sTableDetailsMain").removeClass("hide")
    });

    //convert selected values array's data into a json code
    $("#convertJson").click(function(){
        const myJSON = JSON.stringify(selectValues);
        $('#jsonOutput').val(myJSON);

        //create a json file
        let link = $("#downloadJson");
        let name = 'tableOutput';
        let text = myJSON
        link.attr('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        link.attr('download', `${name.toLowerCase()}.json`);

        $(".jsonWrap").removeClass("hide")
    });
	
	
	//copy json code
	$("#sqlQry").click(function(){
		
		let query = "";
		
		for (let i = 0; i < selectValues.length; i++) {
		  for (let j = 0; j < selectValues[i].length; j++) {
			if (typeof selectValues[i][j] === 'object') {
			  let attributes = " "
			  for (let k = 0; k < selectValues[i][j].length; k++) {
				
				table_name = selectValues[i][0];
				value1 = selectValues[i][j][k].attribute
				value2 = selectValues[i][j][k].dataType
				value3 = selectValues[i][j][k].dSensitivity
				value4 = selectValues[i][j][k].filterRule
				attributes = attributes + value1 + ", "
				//query += "INSERT INTO "+ table_name + "(attribute, dataType, dSensitivity, filterRule) VALUES ( "+ value1 +","+ value2 +","+ value3 +","+ value4 +");\n";

			  }

			  query += "SELECT" + attributes   + "FROM "+ table_name +";\n";

			} else {
			  console.log(selectValues[i][j]);
			}
		  }
		}
		
		const mySQL = query;
		
		$('#jsonOutput').val(mySQL);
		//create a json file
        let link = $("#downloadJson");
        let name = 'sqlQuery';
        let text = mySQL
        link.attr('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
        link.attr('download', `${name.toLowerCase()}.sql`);

        $(".jsonWrap").removeClass("hide")
	});

    //copy json code
    $("#jsonCopy").click(function(){
        let copyText = $('#jsonOutput')
        copyText.select();
        document.execCommand("copy");
    });
	
	
	$("#myButton").click(function() {
          alert("Button clicked!");
        });
	
	
	
	
});

