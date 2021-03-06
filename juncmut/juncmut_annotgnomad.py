#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:30:10 2019

@author: genome
"""
def juncmut_annotgnomad(input_file, output_file, gnomad, genome_id):
    import pysam

    db = gnomad
    tb = pysam.TabixFile(db)

    with open(input_file, 'r') as hin:
        with open(output_file,'w') as hout:
            header = hin.readline().rstrip('\n')
            new_header = header + "\tgnomAD\tgnomAD_AF\n"
            hout.write(new_header)

            for line in hin: # one SJ
                line = line.rstrip('\n')
                junc_record = line
                F = line.split('\t')
                mut_key = F[0].split(',')
                chrmo = mut_key[0]
                pos = mut_key[1]
                mut_ref = mut_key[2]
                mut_alt = mut_key[3]
                
                c = chrmo.replace('chr', '')

                if c != "Y":
                    out_record = ""
                    if genome_id == "hg19":
                        chr = str(c)
                    else:
                        chr = "chr" + str(c)
                    #rows = tb.fetch(chr, int(F[13]) - 1, int(F[13]))
                    #skip val
                    rows = tb.fetch(chr, int(pos) - 1, int(pos))

                    cur_AF = 0.0
                    cur_allele = "-"
                    if rows is not None:
                        for row in rows:
                            srow=str(row)
                            record = srow.split('\t')
                            #if mut_ref == record[3] and mut_alt == record[4]:
                            #skip val
                            if mut_ref == record[3] and mut_alt == record[4]:
                                allele = record[3]+">"+record[4]
                                infos = record[7].split(';')
                                for info in infos:
                                    if info.startswith("AF="):
                                        cur_AF = float(info.replace("AF=", ''))
                                        cur_allele = allele

                                break
                    
                    out_record = junc_record + "\t" + cur_allele + "\t" + str(cur_AF) +"\n"
                    hout.write(out_record)


                elif c in ["Y"]:
                    out_record = junc_record + "\tna\t0\n"
                    hout.write(out_record)


if __name__== "__main__":
    import argparse

    parser = argparse.ArgumentParser() #make a parser

    parser.add_argument("--input_file", metavar = "input_file", default = None, type = str,
                            help = "input file")
    parser.add_argument("--output_file", metavar = "output_file", default = "my sample", type = str,
                            help = "output file")
    parser.add_argument("--gnomad", metavar = "gnomad", default = None, type = str,
                            help = "/path/to/gnomad_db")
    parser.add_argument("--genome_id", choices = ["hg19", "hg38"], default = "hg38",
                              help = "Genome id used for selecting snp data (default: %(default)s)")

    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    gnomad = args.gnomad
    genome_id = args.genome_id

    juncmut_annotgnomad(input_file, output_file, gnomad, genome_id)
