html_style = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>References</title>
    <!-- Bootstrap CSS for Styling -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    <!-- FontAwesome for Icons -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f7fc;
            margin: 20px;
        }
        table {
            width: 100%;
            margin-top: 20px;
            border-radius: 10px;
            overflow: hidden;
        }
        .table th, .table td {
            text-align: center;
            vertical-align: middle;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .table-hover tbody tr:hover {
            background-color: #f1f1f1;
        }
        .table-striped tbody tr:nth-of-type(odd) {
            background-color: #f9f9f9;
        }
        .table-dark th, .table-dark td {
            background-color: #343a40;
            color: white;
        }
        .dataTables_wrapper .dataTables_paginate .paginate_button {
            border: none;
            padding: 5px 10px;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
        }
        .dataTables_wrapper .dataTables_paginate .paginate_button:hover {
            background-color: #0056b3;
        }
        .dataTables_wrapper .dataTables_filter input {
            margin-left: 0.5em;
            padding: 5px;
            border-radius: 5px;
        }
        .dataTables_length select {
            width: auto;
            padding: 5px;
            border-radius: 5px;
        }
        .dataTables_info {
            color: #333;
        }
        /* Sticky header */
        thead {
            position: sticky;
            top: 0;
            background-color: #343a40;
            z-index: 1;
        }
        .dark-mode {
            background-color: #343a40;
            color: white;
        }
        .light-mode {
            background-color: #f4f7fc;
            color: black;
        }
    </style>
</head>
<body>
    <h1><i class="fas fa-book"></i> References</h1>
    <table id="referencesTable" class="table table-striped table-bordered table-hover table-dark">
        <thead>
            <tr>
"""
